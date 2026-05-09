import urllib.request, os
os.makedirs('imagenes', exist_ok=True)
imagenes = {
    "coalbrookdale.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Philip_James_de_Loutherbourg_-_Coalbrookdale_by_Night_-_Google_Art_Project.jpg/1280px-Philip_James_de_Loutherbourg_-_Coalbrookdale_by_Night_-_Google_Art_Project.jpg",
    "watt_engine.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/SteamEngine_Boulton%26Watt_1784.png/800px-SteamEngine_Boulton%26Watt_1784.png",
    "jacquard_loom.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Jacquard_loom_p1040320.jpg/800px-Jacquard_loom_p1040320.jpg",
    "ford_assembly.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Ford_assembly_line_-_1913.jpg/1280px-Ford_assembly_line_-_1913.jpg",
    "ibm_pc.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IBM_PC_5150.jpg/1024px-IBM_PC_5150.jpg",
    "karl_marx.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Karl_Marx_001.jpg/800px-Karl_Marx_001.jpg",
    "locomotora.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Stephenson%27s_Rocket_in_the_Science_Museum_%28cropped%29.jpg/800px-Stephenson%27s_Rocket_in_the_Science_Museum_%28cropped%29.jpg",
    "london_slums.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Dore_London.jpg/1024px-Dore_London.jpg",
    "trabajo_infantil.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Lewis_Hine%2C_Oyster_fishers%2C_Biloxi%2C_Mississippi%2C_1911.jpg/1024px-Lewis_Hine%2C_Oyster_fishers%2C_Biloxi%2C_Mississippi%2C_1911.jpg",
    "thomas_edison.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Thomas_Edison2.jpg/800px-Thomas_Edison2.jpg",
    "nikola_tesla.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/N.Tesla.JPG/800px-N.Tesla.JPG",
    "wright_vuelo.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/First_flight2.jpg/1280px-First_flight2.jpg",
    "eniac.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Eniac.jpg/1280px-Eniac.jpg",
    "internet_map.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Internet_map_1024.jpg/1024px-Internet_map_1024.jpg",
    "robot_kuka.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/KUKA_robot_for_car_production.jpg/1024px-KUKA_robot_for_car_production.jpg",
    "deep_blue.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/800px-Deep_Blue.jpg",
    "smartphone.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Samsung_Galaxy_S22%2C_photographed_by_Dhruv_Malhotra_%28Unsplash%29.jpg/800px-Samsung_Galaxy_S22%2C_photographed_by_Dhruv_Malhotra_%28Unsplash%29.jpg",
    "bombilla.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Gluehlampe_01_KMJ.png/600px-Gluehlampe_01_KMJ.png",
}
for nombre, url in imagenes.items():
    print(f'Descargando {nombre}...')
    try:
        urllib.request.urlretrieve(url, f'imagenes/{nombre}')
    except Exception as e:
        print(f'  Error: {e}')
print('¡Listo!')