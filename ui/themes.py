def apply_theme():
    with dpg.theme() as main_theme:
        # Color scheme: Dark blue with neon accents
        with dpg.theme_component():
            # Window styling
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (25, 25, 40))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (15, 15, 30))
            
            # Text and controls
            dpg.add_theme_color(dpg.mvThemeCol_Text, (220, 240, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 120, 215))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 150, 255))
            
            # Special elements
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (40, 40, 60, 180))
            dpg.add_theme_color(dpg.mvThemeCol_Header, (0, 80, 120))
            
            # Transparent elements
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)
            dpg.add_theme_style(dpg.mvStyleVar_Alpha, 0.95)
    
    dpg.bind_theme(main_theme)
