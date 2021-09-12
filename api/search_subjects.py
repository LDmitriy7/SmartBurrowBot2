from config.subjects import ALL_SUBJECTS


def get_fit_subjects(query: str, limit: int) -> set[str]:
    fit_subjects = set()

    for subject in ALL_SUBJECTS:
        if query.lower() in subject.lower():
            fit_subjects.add(subject)
            if len(fit_subjects) >= limit:
                break
    return fit_subjects
