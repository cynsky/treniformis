from update_filter_lists import update_mappings
from update_filter_lists import update_base_lists
from update_filter_lists import update_derived_lists
from update_filter_lists import update_fishing_vessel_lists
from update_filter_lists import update_mapped_lists
from update_readmes import update_readmes


def update_all():
    update_mappings()
    update_base_lists()
    update_derived_lists()
    update_fishing_vessel_lists()
    update_mapped_lists()
    update_readmes()


if __name__ == "__main__":
    update_all()