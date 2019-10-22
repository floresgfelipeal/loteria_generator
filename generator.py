"""Mexican Loteria Boards Generator
"""

import os
import random
import sys

from fpdf import Template


class LoteriaGenerator:
    CARDS = os.listdir('cards')
    ELEMENTS_P = [
        {'name': 'title_1', 'type': 'T', 'x1': 26.03, 'y1': 16.0, 'x2': 107.722,
         'y2': 25.0, 'font': 'Times', 'size': 18.0, 'bold': 1, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': '', 'priority': 0},
        {'name': 'board_number_1', 'type': 'T', 'x1': 107.722, 'y1': 16.0,
         'x2': 189.414, 'y2': 25.0, 'font': 'Times', 'size': 18.0, 'bold': 1,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'R', 'text': '', 'priority': 0},

        {'name': 'container', 'type': 'B', 'x1': 26.03, 'y1': 25.0,
         'x2': 189.414, 'y2': 264.4, 'font': 'Arial', 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 0},
        {'name': 'box_1', 'type': 'B', 'x1': 28.57, 'y1': 27.55, 'x2': 66.35,
         'y2': 84.21, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_2', 'type': 'B', 'x1': 68.91, 'y1': 27.55, 'x2': 106.69,
         'y2': 84.21, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_3', 'type': 'B', 'x1': 109.22, 'y1': 27.55, 'x2': 147.1,
         'y2': 84.21, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_4', 'type': 'B', 'x1': 149.54, 'y1': 27.55, 'x2': 187.42,
         'y2': 84.21, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_5', 'type': 'B', 'x1': 28.57, 'y1': 86.76, 'x2': 66.35,
         'y2': 143.41, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_6', 'type': 'B', 'x1': 68.91, 'y1': 86.76, 'x2': 106.69,
         'y2': 143.41, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_7', 'type': 'B', 'x1': 109.22, 'y1': 86.76,
         'x2': 147.1, 'y2': 143.41, 'font': 'Arial', 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 1},
        {'name': 'box_8', 'type': 'B', 'x1': 149.54, 'y1': 86.76, 'x2': 187.42,
         'y2': 143.41, 'font': 'Arial', 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 1},
        {'name': 'box_9', 'type': 'B', 'x1': 28.57, 'y1': 145.94, 'x2': 66.35,
         'y2': 202.59, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_10', 'type': 'B', 'x1': 68.91, 'y1': 145.94, 'x2': 106.69,
         'y2': 202.59, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_11', 'type': 'B', 'x1': 109.22, 'y1': 145.94,
         'x2': 147.1, 'y2': 202.59, 'font': 'Arial', 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 1},
        {'name': 'box_12', 'type': 'B', 'x1': 149.54, 'y1': 145.94,
         'x2': 187.42, 'y2': 202.59, 'font': 'Arial', 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 1},
        {'name': 'box_13', 'type': 'B', 'x1': 28.57, 'y1': 205.19, 'x2': 66.35,
         'y2': 261.84, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_14', 'type': 'B', 'x1': 68.91, 'y1': 205.19, 'x2': 106.69,
         'y2': 261.84, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_15', 'type': 'B', 'x1': 109.22, 'y1': 205.19, 'x2': 147.1,
         'y2': 261.84, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box_16', 'type': 'B', 'x1': 149.54, 'y1': 205.19,
         'x2': 187.42, 'y2': 261.84, 'font': 'Arial', 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 1},

        {'name': 'img_1', 'type': 'I', 'x1': 28.57, 'y1': 27.55, 'x2': 66.35,
         'y2': 84.21, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_2', 'type': 'I', 'x1': 68.91, 'y1': 27.55, 'x2': 106.69,
         'y2': 84.21, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_3', 'type': 'I', 'x1': 109.22, 'y1': 27.55, 'x2': 147.1,
         'y2': 84.21, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_4', 'type': 'I', 'x1': 149.54, 'y1': 27.55, 'x2': 187.42,
         'y2': 84.21, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_5', 'type': 'I', 'x1': 28.57, 'y1': 86.76, 'x2': 66.35,
         'y2': 143.41, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_6', 'type': 'I', 'x1': 68.91, 'y1': 86.76, 'x2': 106.69,
         'y2': 143.41, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_7', 'type': 'I', 'x1': 109.22, 'y1': 86.76,
         'x2': 147.1, 'y2': 143.41, 'font': None, 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 0},
        {'name': 'img_8', 'type': 'I', 'x1': 149.54, 'y1': 86.76, 'x2': 187.42,
         'y2': 143.41, 'font': None, 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 0},
        {'name': 'img_9', 'type': 'I', 'x1': 28.57, 'y1': 145.94, 'x2': 66.35,
         'y2': 202.59, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_10', 'type': 'I', 'x1': 68.91, 'y1': 145.94, 'x2': 106.69,
         'y2': 202.59, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_11', 'type': 'I', 'x1': 109.22, 'y1': 145.94,
         'x2': 147.1, 'y2': 202.59, 'font': None, 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 0},
        {'name': 'img_12', 'type': 'I', 'x1': 149.54, 'y1': 145.94,
         'x2': 187.42, 'y2': 202.59, 'font': None, 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 0},
        {'name': 'img_13', 'type': 'I', 'x1': 28.57, 'y1': 205.19, 'x2': 66.35,
         'y2': 261.84, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_14', 'type': 'I', 'x1': 68.91, 'y1': 205.19, 'x2': 106.69,
         'y2': 261.84, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_15', 'type': 'I', 'x1': 109.22, 'y1': 205.19, 'x2': 147.1,
         'y2': 261.84, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_16', 'type': 'I', 'x1': 149.54, 'y1': 205.19,
         'x2': 187.42, 'y2': 261.84, 'font': None, 'size': 0.0, 'bold': 0,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'I', 'text': None, 'priority': 0}
    ]
    ELEMENTS_L = [
        {'name': 'title_1', 'type': 'T', 'x1': 10.5, 'y1': 13.52, 'x2': 74.25,
         'y2': 14.32, 'font': 'Times', 'size': 14.0, 'bold': 1, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': '', 'priority': 0},
        {'name': 'board_number_1', 'type': 'T', 'x1': 75.25, 'y1': 13.52,
         'x2': 139.2, 'y2': 14.32, 'font': 'Times', 'size': 14.0, 'bold': 1,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'R', 'text': '', 'priority': 0},
        {'name': 'title_2', 'type': 'T', 'x1': 140.2, 'y1': 13.52, 'x2': 203.95,
         'y2': 14.32, 'font': 'Times', 'size': 14.0, 'bold': 1, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': '', 'priority': 0},
        {'name': 'board_number_2', 'type': 'T', 'x1': 204.95, 'y1': 13.52,
         'x2': 268.7, 'y2': 14.32, 'font': 'Times', 'size': 14.0, 'bold': 1,
         'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0,
         'align': 'R', 'text': '', 'priority': 0},
        {'name': 'container1', 'type': 'B', 'x1': 10.5, 'y1': 18.0, 'x2': 139.2,
         'y2': 206.05, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'container2', 'type': 'B', 'x1': 140.2, 'y1': 18.0,
         'x2': 268.9,
         'y2': 206.05, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},

        {'name': 'box1_1', 'type': 'B', 'x1': 12.5, 'y1': 20.0, 'x2': 42.17,
         'y2': 64.51, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_2', 'type': 'B', 'x1': 44.17, 'y1': 20.0, 'x2': 73.84,
         'y2': 64.51, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_3', 'type': 'B', 'x1': 75.84, 'y1': 20.0, 'x2': 105.515,
         'y2': 64.51, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_4', 'type': 'B', 'x1': 107.515, 'y1': 20.0, 'x2': 137.19,
         'y2': 64.51, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_5', 'type': 'B', 'x1': 12.5, 'y1': 66.51, 'x2': 42.17,
         'y2': 111.024, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_6', 'type': 'B', 'x1': 44.17, 'y1': 66.51, 'x2': 73.84,
         'y2': 111.024, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_7', 'type': 'B', 'x1': 75.84, 'y1': 66.51, 'x2': 105.515,
         'y2': 111.024, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_8', 'type': 'B', 'x1': 107.515, 'y1': 66.51,
         'x2': 137.19,
         'y2': 111.024, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_9', 'type': 'B', 'x1': 12.5, 'y1': 113.024, 'x2': 42.17,
         'y2': 157.536, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_10', 'type': 'B', 'x1': 44.17, 'y1': 113.024,
         'x2': 73.84,
         'y2': 157.536, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_11', 'type': 'B', 'x1': 75.84, 'y1': 113.024,
         'x2': 105.515,
         'y2': 157.536, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_12', 'type': 'B', 'x1': 107.515, 'y1': 113.024,
         'x2': 137.19,
         'y2': 157.536, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_13', 'type': 'B', 'x1': 12.5, 'y1': 159.536, 'x2': 42.17,
         'y2': 203.6872, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_14', 'type': 'B', 'x1': 44.17, 'y1': 159.536,
         'x2': 73.84,
         'y2': 203.6872, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_15', 'type': 'B', 'x1': 75.84, 'y1': 159.536,
         'x2': 105.515,
         'y2': 203.6872, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box1_16', 'type': 'B', 'x1': 107.515, 'y1': 159.536,
         'x2': 137.19,
         'y2': 203.6872, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_1', 'type': 'B', 'x1': 142.2, 'y1': 20.0, 'x2': 171.87,
         'y2': 64.51, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_2', 'type': 'B', 'x1': 172.87, 'y1': 20.0, 'x2': 203.54,
         'y2': 64.51, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_3', 'type': 'B', 'x1': 205.54, 'y1': 20.0, 'x2': 234.7,
         'y2': 64.51, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_4', 'type': 'B', 'x1': 236.7, 'y1': 20.0, 'x2': 266.89,
         'y2': 64.51, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_5', 'type': 'B', 'x1': 142.2, 'y1': 66.51, 'x2': 171.87,
         'y2': 111.024, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_6', 'type': 'B', 'x1': 172.87, 'y1': 66.51, 'x2': 203.54,
         'y2': 111.024, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_7', 'type': 'B', 'x1': 205.54, 'y1': 66.51, 'x2': 234.7,
         'y2': 111.024, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_8', 'type': 'B', 'x1': 236.7, 'y1': 66.51, 'x2': 266.89,
         'y2': 111.024, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_9', 'type': 'B', 'x1': 142.2, 'y1': 113.024,
         'x2': 171.87,
         'y2': 157.536, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_10', 'type': 'B', 'x1': 172.87, 'y1': 113.024,
         'x2': 203.54,
         'y2': 157.536, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_11', 'type': 'B', 'x1': 205.54, 'y1': 113.024,
         'x2': 234.7,
         'y2': 157.536, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_12', 'type': 'B', 'x1': 236.7, 'y1': 113.024,
         'x2': 266.89,
         'y2': 157.536, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_13', 'type': 'B', 'x1': 142.2, 'y1': 159.536,
         'x2': 171.87,
         'y2': 203.6872, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_14', 'type': 'B', 'x1': 172.87, 'y1': 159.536,
         'x2': 203.54,
         'y2': 203.6872, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_15', 'type': 'B', 'x1': 205.54, 'y1': 159.536,
         'x2': 234.7,
         'y2': 203.6872, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},
        {'name': 'box2_16', 'type': 'B', 'x1': 236.7, 'y1': 159.536,
         'x2': 266.89,
         'y2': 203.6872, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 1},

        {'name': 'img_1', 'type': 'I', 'x1': 12.5, 'y1': 20.0, 'x2': 42.17,
         'y2': 64.51, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_2', 'type': 'I', 'x1': 44.17, 'y1': 20.0, 'x2': 73.84,
         'y2': 64.51, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_3', 'type': 'I', 'x1': 75.84, 'y1': 20.0, 'x2': 105.515,
         'y2': 64.51, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_4', 'type': 'I', 'x1': 107.515, 'y1': 20.0, 'x2': 137.19,
         'y2': 64.51, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_5', 'type': 'I', 'x1': 12.5, 'y1': 66.51, 'x2': 42.17,
         'y2': 111.024, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_6', 'type': 'I', 'x1': 44.17, 'y1': 66.51, 'x2': 73.84,
         'y2': 111.024, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_7', 'type': 'I', 'x1': 75.84, 'y1': 66.51, 'x2': 105.515,
         'y2': 111.024, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_8', 'type': 'I', 'x1': 107.515, 'y1': 66.51, 'x2': 137.19,
         'y2': 111.024, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_9', 'type': 'I', 'x1': 12.5, 'y1': 113.024, 'x2': 42.17,
         'y2': 157.536, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_10', 'type': 'I', 'x1': 44.17, 'y1': 113.024, 'x2': 73.84,
         'y2': 157.536, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_11', 'type': 'I', 'x1': 75.84, 'y1': 113.024,
         'x2': 105.515,
         'y2': 157.536, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_12', 'type': 'I', 'x1': 107.515, 'y1': 113.024,
         'x2': 137.19,
         'y2': 157.536, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_13', 'type': 'I', 'x1': 12.5, 'y1': 159.536, 'x2': 42.17,
         'y2': 203.6872, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_14', 'type': 'I', 'x1': 44.17, 'y1': 159.536, 'x2': 73.84,
         'y2': 203.6872, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_15', 'type': 'I', 'x1': 75.84, 'y1': 159.536,
         'x2': 105.515,
         'y2': 203.6872, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_16', 'type': 'I', 'x1': 107.515, 'y1': 159.536,
         'x2': 137.19,
         'y2': 203.6872, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},

        {'name': 'img_17', 'type': 'I', 'x1': 142.2, 'y1': 20.0, 'x2': 171.87,
         'y2': 64.51, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_18', 'type': 'I', 'x1': 172.87, 'y1': 20.0, 'x2': 203.54,
         'y2': 64.51, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_19', 'type': 'I', 'x1': 205.54, 'y1': 20.0, 'x2': 234.7,
         'y2': 64.51, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_20', 'type': 'I', 'x1': 236.7, 'y1': 20.0, 'x2': 266.89,
         'y2': 64.51, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_21', 'type': 'I', 'x1': 142.2, 'y1': 66.51, 'x2': 171.87,
         'y2': 111.024, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_22', 'type': 'I', 'x1': 172.87, 'y1': 66.51, 'x2': 203.54,
         'y2': 111.024, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_23', 'type': 'I', 'x1': 205.54, 'y1': 66.51, 'x2': 234.7,
         'y2': 111.024, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_24', 'type': 'I', 'x1': 236.7, 'y1': 66.51, 'x2': 266.89,
         'y2': 111.024, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_25', 'type': 'I', 'x1': 142.2, 'y1': 113.024,
         'x2': 171.87,
         'y2': 157.536, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_26', 'type': 'I', 'x1': 172.87, 'y1': 113.024,
         'x2': 203.54,
         'y2': 157.536, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_27', 'type': 'I', 'x1': 205.54, 'y1': 113.024,
         'x2': 234.7,
         'y2': 157.536, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_28', 'type': 'I', 'x1': 236.7, 'y1': 113.024,
         'x2': 266.89,
         'y2': 157.536, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_29', 'type': 'I', 'x1': 142.2, 'y1': 159.536,
         'x2': 171.87,
         'y2': 203.6872, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_30', 'type': 'I', 'x1': 172.87, 'y1': 159.536,
         'x2': 203.54,
         'y2': 203.6872, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_31', 'type': 'I', 'x1': 205.54, 'y1': 159.536,
         'x2': 234.7,
         'y2': 203.6872, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0},
        {'name': 'img_32', 'type': 'I', 'x1': 236.7, 'y1': 159.536,
         'x2': 266.89,
         'y2': 203.6872, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0,
         'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
         'text': None, 'priority': 0}
    ]

    def __init__(self, orientation='portrait', title='LOTERIA', numbered=True):
        self.current_board = 1
        self.numbered = numbered

        if len(title) <= 20:
            self.title = title
        else:
            raise self.error(f'Title length is too long: {len(title)}')

        if orientation == 'portrait':
            self.boards_per_page = 1
            self.file = Template(format='Letter',
                                 elements=LoteriaGenerator.ELEMENTS_P,
                                 title='Loteria', orientation=orientation)
        elif orientation == 'landscape':
            self.boards_per_page = 2
            self.file = Template(format='Letter',
                                 elements=LoteriaGenerator.ELEMENTS_L,
                                 title='Loteria', orientation=orientation)
        else:
            raise self.error(f'Incorrect Orientation: {orientation}')

    def error(self, msg):
        """Fatal error"""
        raise RuntimeError(f'LoteriaGenerator Error: {msg}')

    def add_page(self):
        """Adds a page to the PDF file based on the selected template with
           16 or 32 randomized loteria cards images.
        """

        self.file.add_page()
        for i in range(self.boards_per_page):
            sample = random.sample(LoteriaGenerator.CARDS, 16)
            self.file[f'title_{i+1}'] = self.title

            if self.numbered:
                self.file[f'board_number_{i+1}'] = f'TABLA {self.current_board}'
                self.current_board += 1

            for num, card in enumerate(sample, start=1):
                self.file[f'img_{i*16+num}'] = f'cards/{card}'

    def add_n_pages(self, n_pages):
        """Adds 'n_pages' to the PDF file based on the selected template with
           16 or 32 randomized loteria cards images.
        """
        for _ in range(n_pages):
            self.add_page()

    def render_pdf(self, file_path):
        """Saves the PDF file to disk on the selected file_path"""

        self.file.render(file_path)


def main(orientation, n_pages, file_path, title):
    if len(title) > 20:
        sys.exit('Error: Title should have 20 characters or less.')

    orientation_low = orientation.lower()
    if orientation_low == '-p' or orientation_low == '--portrait':
        gen = LoteriaGenerator('portrait', title.upper())
    elif orientation_low == '-l' or orientation_low == '--landscape':
        gen = LoteriaGenerator('landscape', title.upper())
    else:
        sys.exit('Error: Invalid Orientation. Type --h for usage.')

    if 0 >= n_pages:
        sys.exit('Number of pages should be > 0')
    elif n_pages > 500:
        sys.exit('Number of pages should be <= 500')
    else:
        gen.add_n_pages(n_pages)

    try:
        gen.render_pdf(file_path)
    except OSError as err:
        print(err)


if __name__ == '__main__':
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print('Usage: generator.py [-p | -l] [number_of_pages] [file_path] '
              '[title]\n\n'
              '-h, --help       Shows this help message.\n\n'
              '-p, --portrait\n'
              '-l, --landscape  Selects the orientation for the pdf file.'
              '\n\n'
              'number_of_pages  Min. 1 Max. 500.\n\n'
              'file_path        Path where the pdf file will be generated.\n'
              'title            Max. 20 characters. If the title contains '
              'whitespaces it should be quoted.')
    else:
        try:
            num = int(sys.argv[2])
        except ValueError:
            sys.exit('Error: Invalid number. Type --h for usage.')
        main(sys.argv[1], num, sys.argv[3], sys.argv[4])
