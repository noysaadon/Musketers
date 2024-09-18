from login.enums import WhoNeedHelpVolunteer


def dto_to_backend(dto_from_front):
    mapping = {
        'char_child': WhoNeedHelpVolunteer.CHILD.value,
        'vol_child': WhoNeedHelpVolunteer.CHILD.value,
        'char_singleparent': WhoNeedHelpVolunteer.SINGEL_PARENT.value,
        'vol_singleparent': WhoNeedHelpVolunteer.SINGEL_PARENT.value,
        'char_elders': WhoNeedHelpVolunteer.ELDERS.value,
        'vol_elders': WhoNeedHelpVolunteer.ELDERS.value,
    }

    # Find the matching key in the mapping
    for key in dto_from_front:
        if key in mapping:
            return mapping[key]

    return None

