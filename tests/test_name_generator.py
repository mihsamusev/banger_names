
from banger_names.name_generator import combine_name_parts, format_name


def test_format_name():
    assert format_name("") == ""
    assert format_name("Martin") == "martin"
    assert format_name("George R. Martin") == "martin"


def test_combine_name_parts():
    assert combine_name_parts(["part1"]) == "part1"
    assert combine_name_parts(["part1", "part2"]) == "part1_part2"