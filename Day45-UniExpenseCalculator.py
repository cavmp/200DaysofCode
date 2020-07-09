import matplotlib.pyplot as plt
import numpy as np

def main():
    print('Welcome to Uni Expense Calculator! \n')
    print('This tool can be used by high school seniors accepted to university.')
    print("A series of question will be asked that will take in the university's expenses.")
    print('Before starting, you have to have information about tuition, grants, loans, and housing ready.')
    print('This tool will give you the most accurate estimate and hope to keep you financially prepared.\n')
    input('Press enter to begin: ')

    print('\nPlease give the following amounts for the expense categories listed.')
    print('NOTE: If you have no expenses for a category, input 0. Please only enter numbers.\n')

    tuition = float(input('Tuition: '))
    housing = float(input('Housing: '))
    food = float(input('Food Costs: '))
    transportation = float(input('Transportation: '))
    materials = float(input('Materials (books, school supplies, etc): '))
    miscellaneous = float(input('Miscellaneous Expenses: '))
    scholarships = float(input('Grants and Scholarships: '))
    loans = float(input('Loans: '))
    aid = float(input('Other Aid Awarded: '))

    before_aid = tuition + housing + food + transportation + materials + miscellaneous
    total_aid = scholarships + loans + aid
    print('\nYour total expenses before applying financial aid is:', before_aid)
    print('Your total aid is:', total_aid)

    print('\nHow much financial aid would you like to use from each category?\n')

    scholarships1 = float(input('Grants and Scholarships: '))
    if scholarships1 > scholarships:
        print('\nThe amount of aid entered for scholarships is more than the initial amount entered.')
        print('Please enter an amount less than or equal to', scholarships)
        scholarships1 = float(input('\nGrants and Scholarships: '))
    loans1 = float(input('Loans: '))
    if loans1 > loans:
        print('\nThe amount of aid entered for scholarships is more than the initial amount entered.')
        print('Please enter an amount less than or equal to', loans)
        loans1 = float(input('\nLoans: '))
    aid1 = float(input('Other Aid Awarded: '))
    if aid1 > aid:
        print('\nThe amount of aid entered for other aids is more than the initial amount entered.')
        print('Please enter an amount less than or equal to', aid)
        aid1 = float(input('\nOther Aid Awarded: '))

    total_updated_aid = scholarships1 + loans1 + aid1

    print('\nOut of the aid you would like to use, how much of it would apply to each expense category?\n')

    aidfor_tuition = float(input('Tuition: '))
    if aidfor_tuition > tuition:
        print('\nThe amount of aid entered for tuition was greater than the initial amount entered.')
        excess = aidfor_tuition-tuition
        print('This is the amount of extra aid you applied:', excess)
        aidfor_tuition = float(input('\nTuition: '))
    if total_updated_aid < aidfor_tuition:
        print('\nYou have exceeded the amount entered for your total  aid.')
        print('Please enter a number less than', total_updated_aid)
        aidfor_tuition = float(input('\nTuition: '))
    aidfor_housing = float(input('Housing: '))
    if aidfor_housing > housing:
        print('\nThe amount of aid entered for housing was greater than the initial amount entered.')
        excess = aidfor_housing-housing
        print('This is the amount of extra aid you applied:', excess)
        aidfor_housing = float(input('\nHousing: '))
    if total_updated_aid < aidfor_housing + aidfor_tuition:
        print('\nYou have exceeded the amount entered for your total  aid.')
        print('Please enter a number less than', total_updated_aid - aidfor_tuition)
        aidfor_housing = float(input('\nHousing: '))
    aidfor_food = float(input('Food Costs: '))
    if aidfor_food > food:
        print('\nThe amount of aid entered for food was greater than the initial amount entered.')
        excess = aidfor_food-food
        print('This is the amount of extra aid you applied:', excess)
        aidfor_food = float(input('\nFood Costs: '))
    if total_updated_aid < aidfor_tuition + aidfor_housing + aidfor_food:
        print('\nYou have exceeded the amount entered for your total  aid.')
        print('Please enter a number less than', total_updated_aid - aidfor_tuition - aidfor_housing)
        aidfor_food = float(input('\nFood Costs: '))
    aidfor_transportation = float(input('Transportation: '))
    if aidfor_transportation > transportation:
        print('\nThe amount of aid entered for transportation was greater than the initial amount entered.')
        excess = aidfor_transportation-transportation
        print('This is the amount of extra aid you applied:', excess)
        aidfor_transportation = float(input('\nTransportation: '))
    if total_updated_aid < aidfor_tuition + aidfor_housing + aidfor_food + aidfor_transportation:
        print('\nYou have exceeded the amount entered for your total  aid.')
        print('Please enter a number less than', total_updated_aid - aidfor_tuition - aidfor_housing - aidfor_food)
        aidfor_transportation = float(input('\nTransportation: '))
    aidfor_materials = float(input('Materials (books, school supplies, etc): '))
    if aidfor_materials > materials:
        print('\nThe amount of aid entered for materials was greater than the initial amount entered.')
        excess = aidfor_materials-materials
        print('This is the amount of extra aid you applied:', excess)
        aidfor_materials = float(input('\nMaterials (books, school supplies, etc): '))
    if total_updated_aid < aidfor_tuition + aidfor_housing + aidfor_food + aidfor_transportation + aidfor_materials:
        print('\nYou have exceeded the amount entered for your total  aid.')
        print('Please enter a number less than', total_updated_aid - aidfor_tuition - aidfor_housing - aidfor_food - aidfor_transportation)
        aidfor_materials = float(input('\nMaterials (books, school supplies, etc): '))
    aidfor_miscellaneous = float(input('Miscellaneous Expenses: '))
    if aidfor_miscellaneous > miscellaneous:
        print('\nThe amount of aid entered for miscellaneous was greater than the initial amount entered.')
        excess = aidfor_miscellaneous-miscellaneous
        print('This is the amount of extra aid you applied:', excess)
        aidfor_miscellaneous = float(input('\nMiscellaneous Expenses: '))
    if total_updated_aid < aidfor_tuition + aidfor_housing + aidfor_food + aidfor_transportation + aidfor_materials + aidfor_miscellaneous:
        print('\nYou have exceeded the amount entered for your total  aid.')
        print('Please enter a number less than', total_updated_aid - aidfor_tuition - aidfor_housing - aidfor_food - aidfor_transportation - aidfor_materials)
        aidfor_miscellaneous = float(input('\nMaterials (books, school supplies, etc): '))

    aid_remaining = total_updated_aid - aidfor_tuition - aidfor_housing - aidfor_food - aidfor_transportation - aidfor_materials - aidfor_miscellaneous
    print('\nThis is the amount of financial aid remaining:', aid_remaining)

    final_tuition = tuition - aidfor_tuition
    final_housing = housing - aidfor_housing
    final_food = food - aidfor_food
    final_transportation = transportation - aidfor_transportation
    final_materials = materials - aidfor_materials
    final_miscellaneous = miscellaneous - aidfor_miscellaneous

    print('\nTotal Expenses:\nTuition Fee:', final_tuition)
    print('Housing:', final_housing)
    print('Food:', final_food)
    print('Transportation:', final_transportation)
    print('Materials:', final_materials)
    print('Miscellaneous:', final_miscellaneous)
    print('\nTotal Added Expenses:', final_tuition + final_housing + final_food + final_transportation + final_materials + final_miscellaneous)

    fig, ax = plt.subplots(figsize=(9, 7), subplot_kw=dict(aspect="equal"))

    value_lbl = ['Tuition', 'Housing', 'Food Costs', 'Transportation', 'Materials', 'Miscellaneous']
    values = [final_tuition, final_housing, final_food, final_transportation, final_materials, final_miscellaneous]

    def func(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(values, autopct=lambda pct: func(pct, values),
                                      textprops=dict(color="w"))

    ax.legend(wedges, value_lbl,
              title="Components:",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Uni Expense Calculator")

    plt.show()


if __name__ == '__main__':
    main()
