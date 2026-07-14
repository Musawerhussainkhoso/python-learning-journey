#9. Compare Two Software Versions
def compare_versions(
    old_features: tuple[str, ...],
    new_features: tuple[str, ...]
) -> tuple[
    tuple[str, ...],
    tuple[str, ...],
    tuple[str, ...]
]:
    """
    Compare features between two software versions.
    """

    added_features = []
    removed_features = []
    unchanged_features = []

    for feature in new_features:
        if feature not in old_features:
            added_features.append(feature)
        else:
            unchanged_features.append(feature)

    for feature in old_features:
        if feature not in new_features:
            removed_features.append(feature)

    return (
        tuple(added_features),
        tuple(removed_features),
        tuple(unchanged_features)
    )


version_1_features = (
    "User Login",
    "Patient Registration",
    "Doctor Search",
    "Appointment Booking",
    "Email Notifications"
)

version_2_features = (
    "User Login",
    "Patient Registration",
    "Doctor Search",
    "Appointment Booking",
    "Google Login",
    "Payment Processing",
    "SMS Notifications"
)

added, removed, unchanged = compare_versions(
    version_1_features,
    version_2_features
)

print("SOFTWARE VERSION COMPARISON")
print("=" * 65)

print("\nAdded features:")
for feature in added:
    print(f"  + {feature}")

print("\nRemoved features:")
for feature in removed:
    print(f"  - {feature}")

print("\nUnchanged features:")
for feature in unchanged:
    print(f"  = {feature}")