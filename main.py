import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import serial


# animation function
def animate(i, data_lst, ser):  # ser is the serial object
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    try:
        flt = float(string)
        data_lst.append(flt)
        data_lst.append(flt)
    except:
        pass
    # Add x and y to lists

    # Limit the data list to 100 values
    data_lst = data_lst[-100:]
    # clear the last frame and draw the next frame
    ax.clear()
    ax.plot(data_lst)
    # Format plot
    ax.set_ylim([0, 1050])
    ax.set_title("Potentiometer Reading Live Plot")
    ax.set_ylabel("Potentiometer Reading")


# create empty list to store data
# create figure and axes objects
data_lst = []
fig, ax = plt.subplots()

# set up the serial line
ser = serial.Serial('COM4', 9600)  # change COM# if necessary
time.sleep(2)
print(ser.name)

# run the animation and show the figure
ani = animation.FuncAnimation(
    fig, animate, frames=100, fargs=(data_lst, ser), interval=100
)
plt.show()

# after the window is closed, close the serial line
ser.close()
print("Serial line closed")
