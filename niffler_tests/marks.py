import pytest


class Pages:
    main_page = pytest.mark.usefixtures("o_main_page")


class TestData:
    category = lambda x: pytest.mark.parametrize("s_category", [x], indirect=True)
    spends = lambda x: pytest.mark.parametrize(
        "spends",
        [x],
        indirect=True,
        ids=lambda param: (
            ", ".join(spending["description"] for spending in param) if isinstance(param, list) else param.get("description", str(param))
        )
    )

