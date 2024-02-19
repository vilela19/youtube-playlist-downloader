def validate_folder_name(name):
    invalid_characters = r'\/:*?"<>|'
    for character in invalid_characters:
        name = name.replace(character, ' - ')
    return name