from banger_names.names import CHEMISTS, DEVICES, ADJECTIVES
import numpy as np

def format_name(name: str) -> str:
    return name.split(" ")[-1].lower()


def combine_name_parts(names: list[str]) -> str:
    return "_".join(names)


def generate_names(count: int) -> list[str]:
    chemist = np.random.choice(CHEMISTS, size=count)
    adjective = np.random.choice(ADJECTIVES, size=count)
    device = np.random.choice(DEVICES, size=count)

    parts = zip(chemist, adjective, device)
    return [combine_name_parts(map(format_name, part)) for part in parts]
