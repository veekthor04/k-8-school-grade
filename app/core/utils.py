from drf_yasg.inspectors import SwaggerAutoSchema


class CustomAutoSchema(SwaggerAutoSchema):
    """Custom SwaggerAutoSchema to add tags to views"""

    def get_tags(self, operation_keys=None) -> list:
        tags = self.overrides.get("tags", None) or getattr(
            self.view, "my_tags", []
        )
        if not tags:
            tags = [operation_keys[0]]

        return tags
