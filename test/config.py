panel_bg = 'transparent'
panel_border = 'none'
real_panel_bg = '#232631'
icon_color = '#e6e6e6'

text_props = {
    'color': icon_color,
    'background-color': real_panel_bg,
    'font-size': '14px',
    'font-family': 'Hack, FontAwesome'
}


def bounds():
    return {'x': 65, 'y': 15, 'w': 1791, 'h': 34}


def render_loop_delay():
    return 1000
    

def init_prop_updaters(tools, props):
    return []


def config(data):
    data.ui.set_bg(data.panel, panel_bg)
    data.ui.set_border(data.panel, panel_border)
    render_logo(data)
    data.layout.addStretch(1)
    render_cpu(data)
    render_mem(data)
    data.layout.addStretch(1)
    render_time(data)
    render_weather(data)
    data.layout.addStretch(1)
    render_network(data)
    render_volume(data)
    render_battery(data)
    data.layout.addStretch(1)
    render_power(data)


def render_logo(data):
    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    lbl = data.ui.add_image(data.layout, __file__, '../res/ubuntu-logo.svg', 4)
    data.ui.recolor_pixmap(lbl.pixmap(), icon_color)
    data.ui.set_bg(lbl, real_panel_bg)
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_cpu(data):
    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf200;', { # cpu
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' 3% ', {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf2db;', { # temp
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'lu', real_panel_bg)
    data.ui.add_center_label(data.layout, ' 20C ', {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)



def render_mem(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf085;', { # mem
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' 786mb ', {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_time(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf073;', { # calendar
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' 9/23/2017 ', {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)
    
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf017;', { # clock
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' 12:33 AM ', {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_weather(data):
    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf0c2;', { # wifi
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' 82° F ', {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)


def render_network(data):
    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf1eb;', { # wifi
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' CentHub ', {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_volume(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf028;', { # volume
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, ' 100% ', {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_battery(data):
    battery_text = '100%'
    if True: # charging
        battery_text += ' [&#xf0e7;]' # bolt

    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, '&#xf240;', { # battery
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'ru', real_panel_bg)

    data.ui.add_slant(data.layout, 'ld', real_panel_bg)
    data.ui.add_center_label(data.layout, battery_text, {
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)


def render_power(data):
    data.ui.add_slant(data.layout, 'lui', real_panel_bg)
    data.ui.add_center_label(data.layout, ' &#xf011; ', { # power
        'css': {**text_props}
    })
    data.ui.add_slant(data.layout, 'rd', real_panel_bg)
