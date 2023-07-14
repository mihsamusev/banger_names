from banger_names.names import CHEMISTS, DEVICES, ADJECTIVES
import random



def format_name(name: str) -> str:
    return name.split(" ")[-1].lower()


def combine_name_parts(names: list[str]) -> str:
    return "_".join(names)


def generate_names(count: int) -> list[str]:
    chemist = random.choices(CHEMISTS, k=count)
    adjective = random.choices(ADJECTIVES, k=count)
    device = random.choices(DEVICES, k=count)

    parts = zip(chemist, adjective, device)
    return [combine_name_parts(map(format_name, part)) for part in parts]