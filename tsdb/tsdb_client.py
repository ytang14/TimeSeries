import asyncio
from .tsdb_serialization import serialize, LENGTH_FIELD_LENGTH, Deserializer
from .tsdb_ops import *
from .tsdb_error import *

class TSDBClient(object):
    """
    The client. This could be used in a python program, web server, or REPL!
    """
    def __init__(self, port=9999):
        self.port = port
        self.deserializer = Deserializer()

    def insert_ts(self, primary_key, ts):
        ts_insert = TSDBOp_InsertTS(primary_key, ts)
        self._send(ts_insert.to_json())

    def upsert_meta(self, primary_key, metadata_dict):
        ts_update = TSDBOp_UpsertMeta(primary_key, metadata_dict)
        self._send(ts_update.to_json())


    def select(self, metadata_dict={},fields=None):
        ts_select = TSDBOp_Select(metadata_dict,fields)
        return self._send(ts_select.to_json())
    
    def add_trigger(self, proc, onwhat, target, arg):
        msg = TSDBOp_AddTrigger(proc, onwhat, target, arg)
        return self._send(msg.to_json())

    def remove_trigger(self, proc, onwhat):
        msg = TSDBOp_RemoveTrigger(proc, onwhat)
        return self._send(msg.to_json())

    # Feel free to change this to be completely synchronous
    # from here onwards. Return the status and the payload
    async def _send_coro(self, msg, loop):
        # Open connection and write the serialized message
        reader, writer = await asyncio.open_connection('', self.port, loop=loop)
        writer.write(serialize(msg))
        # Wait for response
        response = await reader.read(8192)
        # Deserialize response
        self.deserializer.append(response)
        if self.deserializer.ready():
            deserialized_response = self.deserializer.deserialize()
            status = deserialized_response['status']
            payload = deserialized_response['payload']
        # Print out status and payload
        print('C> status:',str(TSDBStatus(status)))
        print('C> payload:',payload)
        print('-----------')
        print('C> writing')

        return status, payload


    #call `_send` with a well formed message to send.
    #once again replace this function if appropriate
    def _send(self, msg):
        loop = asyncio.get_event_loop()
        coro = asyncio.ensure_future(self._send_coro(msg, loop))
        loop.run_until_complete(coro)
        return coro.result()
