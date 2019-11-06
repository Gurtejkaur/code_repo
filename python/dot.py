_nw_n, _n_ne = False, False
_nw_w, _n_c, _ne_e = False, False, False
_w_c, _c_e = False, False
_w_sw, _c_s, _e_se = False, False, False
_sw_s, _s_se = False, False

_current_player = 'X'
_lefttop_owner, _righttop_owner = None, None
_leftbottom_owner, _rightbottom_owner = None, None
def _update_square(sq):
    
    global _lefttop_owner, _righttop_owner, _leftbottom_owner, \
    _rightbottom_owner
    if sq == 'LeftTop' and _lefttop_owner == None \
    and _nw_n and _nw_w and _n_c and _w_c:
        _lefttop_owner = _current_player
        return True
    elif sq == 'RightTop' and _righttop_owner == None \
    and _n_ne and _ne_e and _c_e and _n_c:
        _righttop_owner = _current_player
        return True
    elif sq == 'LeftBottom' and _leftbottom_owner == None \
    and _w_c and _c_s and _sw_s and _w_sw:
        _leftbottom_owner = _current_player
        return True
    elif sq == 'RightBottom' and _rightbottom_owner == None \
    and _c_e and _e_se and _s_se and _c_s:
        _rightbottom_owner = _current_player
        return True
    else:
        return False # Owners unchanged
def _update_squares():
    lt = _update_square('LeftTop')
    rt = _update_square('RightTop')
    lb = _update_square('LeftBottom')
    rb = _update_square('RightBottom')
    return lt or rt or lb or rb
def add_line(line):
    global _nw_n, _n_ne, _nw_w, _n_c, _ne_e, _w_c, _c_e, \
    _w_sw, _c_s, _e_se, _sw_s, _s_se, _current_player,line_added
    
    line_added = False # Unsuccessful by default
    if line == 'Northwest_North' and not _nw_n:
        _nw_n = True
        line_added = True
    elif line == 'North_Northeast' and not _n_ne:
        _n_ne = True
        line_added = True
    elif line == 'Northwest_West' and not _nw_w:
        _nw_w = True
        line_added = True
    elif line == 'North_Center' and not _n_c:
        _n_c = True
        line_added = True
    elif line == 'Northeast_East' and not _ne_e:
        _ne_e = True
        line_added = True
    elif line == 'West_Center' and not _w_c:
        _w_c = True
        line_added = True
    elif line == 'Center_East' and not _c_e:
        _c_e = True
        line_added = True
    elif line == 'West_Southwest' and not _w_sw:
        _w_sw = True
        line_added = True
    elif line == 'Center_South' and not _c_s:
        _c_s = True
        line_added = True
    elif line == 'East_Southeast' and not _e_se:
        _e_se = True
        line_added = True
    elif line == 'Southwest_South' and not _sw_s:
        _sw_s = True
        line_added = True
    elif line == 'South_Southeast' and not _s_se:
        _s_se = True
        line_added = True
    # If the line was added successfully ,
    # check to see if it completes a square
    if line_added and not _update_squares():
        # Turn moves to other player upon a successful move
        if _current_player == 'X' :
            _current_player = 'Y'
        else:
             _current_player = 'X'

    return line_added

def square_owner(sq):
    if sq == 'LeftTop':
        return _lefttop_owner
    elif sq == 'RightTop':
        return _righttop_owner
    elif sq == 'LeftBottom':
        return _leftbottom_owner
    elif sq == 'RightBottom' :
        return _rightbottom_owner
    else:
        return None
def check_line(line):
    if line == 'Northwest_North':
        return _nw_n
    elif line == 'North_Northeast':
        return _n_ne
    elif line == 'Northwest_West' :
        return _nw_w
    elif line == 'North_Center':
        return _n_c
    elif line == 'Northeast_East' :
        return _ne_e
    elif line == 'West_Center':
        return _w_c
    elif line == 'Center_East':
        return _c_e
    elif line == 'West_Southwest' :
        return _w_sw
    elif line == 'Center_South':
        return _c_s
    elif line == 'East_Southeast' :
        return _e_se
    elif line == 'Southwest_South':
        return _sw_s
    elif line == 'South_Southeast':
        return _s_se
    else:
        return False
def winner():
    x_count, y_count = 0, 0
    if _lefttop_owner == 'X' :
        x_count += 1
    elif _lefttop_owner == 'Y':
        y_count += 1
    if _righttop_owner == 'X':
        x_count += 1
    elif _righttop_owner == 'Y':
        y_count += 1
    if _rightbottom_owner == 'X':
        x_count += 1
    elif _rightbottom_owner == 'Y' :
        y_count += 1
    if _leftbottom_owner == 'X':
        x_count += 1
    elif _leftbottom_owner == 'Y':
        y_count += 1
    if x_count + y_count == 4: # All squares filled
        if x_count > y_count:
            return 'X' # Player X won
        elif x_count < y_count:
            return 'Y' # Player Y won
        else:
            return 'Draw' # Tie game, no winner
    else:
        return None
def initialize_board():
    global _nw_n, _n_ne, _nw_w, _n_c, _ne_e, _w_c, _c_e, \
    _w_sw, _c_s, _e_se, _sw_s, _s_se, _current_player, \
    _lefttop_owner, _righttop_owner, \
    _leftbottom_owner, _rightbottom_owner
    _nw_n = _n_ne = _nw_w = _n_c = _ne_e = _w_c = _c_e = _w_sw \
    = _c_s = _e_se = _sw_s = _s_se = False
    _lefttop_owner = _righttop_owner = _leftbottom_owner \
    = _rightbottom_owner = None
    current_player = 'X'
def current_player():
    """ Returns the player whose turn it is to move """
    return _current_player
