import serial
import matplotlib.pyplot as plt

def plot_serial_data(port):
    with serial.Serial(port, 9600) as ser:
        data = []
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                data.append(float(line))
        plt.plot(data)
        plt.show()

if __name__ == '__main__':
    plot_serial_data('COM7')
