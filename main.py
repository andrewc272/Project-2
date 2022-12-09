import name_scrambler
import people




def main():
    people_list = people.make_people()
    scrambled_list = name_scrambler.scramble_list(people_list)

    for i in range(len(people_list)):
        people_list[i].send_mail(f'{people_list[i].get_name()}', f'get a gift for {scrambled_list[i].get_name()}')


if __name__ == '__main__':
    main()
