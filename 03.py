#coding: utf-8

# Created by: Anthony Freeman
# Created on: September 2017
# Created for: ICS3U
import ui

def calculate_button_touch_up_inside(sender):

    length = int(view['lengthbox'].text)
    width = int(view['widthbox'].text)
    
    area = length * width
    perimeter = 2 * (length + width)
    
    view['area_answer'].text = 'The area is: ' + str(area) + ' cm^2'
    view['perimeter_answer'].text = 'The perimeter is: ' + str(perimeter) + ' cm'
    
view = ui.load_view()
view.present('full_screen')
