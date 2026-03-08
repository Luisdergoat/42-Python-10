def spell_combiner(spell1, spell2):

    def combined_spells(*args, **kwargs):
        spell1(*args, **kwargs)
        spell2(*args, **kwargs)
        print("The spells have been combined!")
    return combined_spells


########################################################
######## just funktions to test the Task ###############
########################################################


def fireball(power):
    print(f"The fireball hit the Target and did {power} damage")

def Heal_spell(power):
    print(f"The Target got healed for {power} points")


def main():

    result = spell_combiner(fireball, Heal_spell)  # Example argument
    print(result)  # Should print a tuple with the results of both spells

if __name__ == "__main__":
    main()
