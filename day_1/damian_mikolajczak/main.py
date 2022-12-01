INPUT_DATA_FILE_NAME = 'input.txt'


def main():
    with open(INPUT_DATA_FILE_NAME, 'r') as file:
        content = file.read()
        elves = [elf.split('\n') for elf in content.split('\n\n')]
        total_calories_per_elf = [sum([int(item_calories) for item_calories in elf]) for elf in elves]
        total_calories_per_elf.sort(reverse=True)
        print(f'Max calories carried by single elf: {total_calories_per_elf[0]}')  # Answer for first task
        total_calories_of_top_three_elves = sum(total_calories_per_elf[:3])
        print(f'Total calories of top three elves: {total_calories_of_top_three_elves}')  # Answer for first task


if __name__ == '__main__':
    main()

