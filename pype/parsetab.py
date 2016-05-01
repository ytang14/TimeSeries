
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'BA90F0C8CB04659A4089667E76C36B34'
    
_lr_action_items = {'INPUT':([15,],[21,]),'$end':([1,3,4,5,7,8,18,20,],[-1,-5,0,-4,-2,-3,-6,-7,]),'IMPORT':([2,],[9,]),'ID':([6,9,10,12,13,14,15,16,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,57,58,],[10,11,12,-26,-9,12,22,-28,-27,-8,30,12,12,30,12,41,12,12,45,-17,-11,30,-15,12,-30,-21,12,30,-13,12,12,12,12,56,-18,-10,-14,-29,-20,-24,-12,-25,-22,-23,-19,-16,]),'OUTPUT':([15,],[24,]),'OP_MUL':([15,],[23,]),'OP_DIV':([15,],[25,]),'LPAREN':([0,1,3,5,7,8,10,12,13,14,16,17,18,19,20,21,22,23,24,25,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,47,48,49,50,51,52,54,55,57,58,],[2,2,-5,-4,-2,-3,15,-26,-9,15,-28,-27,-6,-8,-7,29,15,15,29,15,15,15,-17,-11,29,-15,15,-30,-21,15,29,-13,15,15,15,15,-10,-14,-29,-20,-24,-12,-25,-22,-23,-19,-16,]),'RPAREN':([11,12,16,17,21,22,24,30,31,32,33,34,35,36,37,38,39,40,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,],[18,-26,-28,-27,31,36,39,-17,-11,46,-15,49,-30,-21,50,51,-13,52,54,55,-10,-14,-29,-20,-24,-12,-25,57,-22,-23,58,-19,-16,]),'RBRACE':([12,13,14,16,17,19,31,36,39,46,49,50,51,52,54,55,57,],[-26,-9,20,-28,-27,-8,-11,-21,-13,-10,-20,-24,-12,-25,-22,-23,-19,]),'LBRACE':([0,1,3,5,7,8,18,20,],[6,6,-5,-4,-2,-3,-6,-7,]),'STRING':([10,12,13,14,16,17,19,22,23,25,27,28,31,34,35,36,37,39,40,41,42,43,46,48,49,50,51,52,54,55,57,],[16,-26,-9,16,-28,-27,-8,16,16,16,16,16,-11,16,-30,-21,16,-13,16,16,16,16,-10,-29,-20,-24,-12,-25,-22,-23,-19,]),'ASSIGN':([15,],[26,]),'NUMBER':([10,12,13,14,16,17,19,22,23,25,27,28,31,34,35,36,37,39,40,41,42,43,46,48,49,50,51,52,54,55,57,],[17,-26,-9,17,-28,-27,-8,17,17,17,17,17,-11,17,-30,-21,17,-13,17,17,17,17,-10,-29,-20,-24,-12,-25,-22,-23,-19,]),'OP_ADD':([15,],[27,]),'OP_SUB':([15,],[28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,],[1,]),'declaration_list':([21,24,],[32,38,]),'component':([0,1,],[3,7,]),'program':([0,],[4,]),'import_statement':([0,1,],[5,8,]),'parameter_list':([22,23,25,27,28,],[34,37,40,42,43,]),'type':([29,],[44,]),'expression':([10,14,22,23,25,27,28,34,37,40,41,42,43,],[13,19,35,35,35,35,35,48,48,48,53,48,48,]),'declaration':([21,24,32,38,],[33,33,47,47,]),'expression_list':([10,],[14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',7),
  ('statement_list -> statement_list component','statement_list',2,'p_statement_list','parser.py',12),
  ('statement_list -> statement_list import_statement','statement_list',2,'p_statement_list','parser.py',13),
  ('statement_list -> import_statement','statement_list',1,'p_statement_list','parser.py',14),
  ('statement_list -> component','statement_list',1,'p_statement_list','parser.py',15),
  ('import_statement -> LPAREN IMPORT ID RPAREN','import_statement',4,'p_import_statement','parser.py',26),
  ('component -> LBRACE ID expression_list RBRACE','component',4,'p_component','parser.py',30),
  ('expression_list -> expression_list expression','expression_list',2,'p_expression_list','parser.py',34),
  ('expression_list -> expression','expression_list',1,'p_expression_list','parser.py',35),
  ('expression -> LPAREN INPUT declaration_list RPAREN','expression',4,'p_expression_input','parser.py',44),
  ('expression -> LPAREN INPUT RPAREN','expression',3,'p_expression_input','parser.py',45),
  ('expression -> LPAREN OUTPUT declaration_list RPAREN','expression',4,'p_expression_output','parser.py',52),
  ('expression -> LPAREN OUTPUT RPAREN','expression',3,'p_expression_output','parser.py',53),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','parser.py',60),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','parser.py',61),
  ('declaration -> LPAREN type ID RPAREN','declaration',4,'p_declaration','parser.py',70),
  ('declaration -> ID','declaration',1,'p_declaration','parser.py',71),
  ('type -> ID','type',1,'p_type','parser.py',79),
  ('expression -> LPAREN ASSIGN ID expression RPAREN','expression',5,'p_expression_assign','parser.py',83),
  ('expression -> LPAREN ID parameter_list RPAREN','expression',4,'p_expression_parameter_list','parser.py',87),
  ('expression -> LPAREN ID RPAREN','expression',3,'p_expression_parameter_list','parser.py',88),
  ('expression -> LPAREN OP_ADD parameter_list RPAREN','expression',4,'p_op_add_expression','parser.py',96),
  ('expression -> LPAREN OP_SUB parameter_list RPAREN','expression',4,'p_op_sub_expression','parser.py',100),
  ('expression -> LPAREN OP_MUL parameter_list RPAREN','expression',4,'p_op_mul_expression','parser.py',104),
  ('expression -> LPAREN OP_DIV parameter_list RPAREN','expression',4,'p_op_div_expression','parser.py',108),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',112),
  ('expression -> NUMBER','expression',1,'p_expression_num','parser.py',116),
  ('expression -> STRING','expression',1,'p_expression_str','parser.py',120),
  ('parameter_list -> parameter_list expression','parameter_list',2,'p_parameter_list','parser.py',124),
  ('parameter_list -> expression','parameter_list',1,'p_parameter_list','parser.py',125),
]
