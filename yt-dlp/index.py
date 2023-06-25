
import operations as op
import MenuItems as moptions

while True:
    main_menu_option = moptions.main_menu()
    if(main_menu_option == '1'):
        moptions.dwnld_video_options()

    elif(main_menu_option == '2'):
        moptions.dwnld_playlist_options()

    elif(main_menu_option == '3'):
        op.version_check()

    elif(main_menu_option == '4'):
        op.update()

    elif(main_menu_option == '5'):
        break