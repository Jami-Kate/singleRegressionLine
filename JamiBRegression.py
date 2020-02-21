'''
Regression Line of Average Temperature in January, 2000 to now
Data from:  https://www.wunderground.com/history/monthly/us/ct/windsor-locks/KBDL/date/2000-1
2-21-20
'''
#Imports numpy and matplot
import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
   #number of observations
    n = np.size(x);

    #finding the mean of x and y vector
    mean_x, mean_y = np.mean(x), np.mean(y)

    #calculating the least squares
    SS_xy = np.sum(y*x) - n * mean_y * mean_x
    SS_xx = np.sum(x*x) - n * mean_x * mean_x

    #regression coefficents
    slope = SS_xy/SS_xx
    yintercept = mean_y - slope * mean_x

    #return m and b
    return(slope, yintercept)

def plot_regression_line(x, y, b):
    #plotting the actual points as a scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    #predicted response vector
    y_pred = b[0] + b[1] + x

    #plotting the regression plot_regression_line
    plt.plot(x, y_pred, color = "g")

    #putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    #function to show plotting
    plt.show()

def main():
    #observations
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    y = np.array([23.73, 26.01, 34.08, 21.66, 18.25, 24.35, 33.88, 32.12, 30.18, 22.11, 28.03, 23.48, 31.96, 29.6, 24.66, 24.09, 30.29, 32.65, 26.09, 26.28, 33.29])

    # estimated coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: \n b = {} \ \n m = {}".format(b[0], b[1]))

    #plotting regression line
    plot_regression_line(x, y, b)

#make script importable and executables
if __name__ == "__main__":
    main()
