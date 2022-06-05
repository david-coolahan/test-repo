import matplotlib.pyplot as plt


def main():
    # x and y coordinates of each data point
    y_male_coords = [1375, 2047, 2233, 2559, 3265]
    y_female_coords = [945, 2479, 3007, 3398, 4415]
    x_coords = [1970, 1980, 1990, 2000, 2010]

    # building the line graph
    plt.plot(x_coords, y_male_coords, color='black', marker='.', label='Males')
    plt.plot(x_coords, y_female_coords, color='black', marker='.', label='Females')

    # line labels (Male and Female)
    y_offset = 253
    plt.text(x_coords[3], y_male_coords[3] - y_offset, "Males", ha='center')
    plt.text(x_coords[3], y_female_coords[3] + y_offset, "Females", ha='center')

    # configuring x axis and y axis labels
    plt.yticks([945, 4415], ["945", "4415"], color='#79C4E4')
    plt.xticks([1970, 1980, 1990, 2000, 2010], ['1970', '1980', '1990', '2000', '2010'], color='#79C4E4')

    # x axis label
    plt.xlabel("Two-Year College Enrollments\n(in thousands)", loc='left', color='#79C4E4')

    # display graph
    plt.show()


# calling main function
if __name__ == '__main__':
    main()
