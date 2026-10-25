from pyray import *

def main():
    height = 600
    width = 800
    init_window(width, height, "Silly game")

    set_target_fps(60)
    score_a = 0
    score_b = 0
    while not window_should_close():

        begin_drawing()
        clear_background(BLACK)
        score_text = str(score_a) + " - " + str(score_b)
        score_font_size = 25
        draw_text(score_text, int(width / 2), 5, score_font_size, RAYWHITE) #not centered but ok, center later

        end_drawing()

    close_window()

if __name__ == '__main__': #not required for this setup, but using it anyway
    main()
