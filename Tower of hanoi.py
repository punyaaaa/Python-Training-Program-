def tower(disk, source, auxiliary, dest):
    if disk == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    tower(disk - 1, source, dest, auxiliary)
    print(f"Move disk {disk} from {source} to {dest}")
    tower(disk - 1, auxiliary, source, dest)




disk = int(input("Enter the number of disks: "))
print("The sequence of moves involved in the Tower of Hanoi are:")
tower(disk, 'A', 'B', 'C')