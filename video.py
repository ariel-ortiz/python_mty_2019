
def main():
    """Solicita al usuario el número de videos nuevos y viejos
    que rentar. Despliega el costo total de la renta.
    """
    new_videos = int(input('Number of new videos to rent: '))
    old_videos = int(input('Number of old videos to rent: '))    
    total = new_videos * 3 + old_videos * 2
    print(f"Total charge for costumer's video rentals: ${total:.2f}")
    
main()