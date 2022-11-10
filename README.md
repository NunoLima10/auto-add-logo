# Auto-add-logo
> This project was developed to add a logo to all photos in a directory
> ### How to use
> Create an instance of the LogoAdder class with the parameters
>````python
>logo_adder = LogoAdder(
>        "Logo.png", 
>        images_folder, 
>        LogoPosition.center, 
>        logo_size=0.5,
>        logo_angle= 0,
>        x_offset= 100,
>        y_offset= -100
>    )
>````
> ````python
> logo_adder.start()
>````
> After using the start() method, all new images will be placed in the directory named “with_logo”
 ---
> ### Todo list paused(10/11/2022)
> - fix exe file bugs
> - release exe file
