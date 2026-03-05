def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda x: x['power'], mages))
    return {
        'max_power': max(powers, key=lambda x: x),
        'min_power': min(powers, key=lambda x: x),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} "
          f"power) comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))
