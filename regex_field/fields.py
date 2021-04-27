from django.core import checks, exceptions
from django.db.models.fields import CharField

from django.core import validators
import re


class RegexField(CharField):

    # def __init__(self, *args, db_collation=None, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.validators.append(validators.RegexValidator())

    def validate(self, value, model_instance):
        """
        Use custom validation for regex field.
        """

        if not self.editable:
            # Skip validation for non-editable fields.
            return

        if value == '[':
            raise exceptions.ValidationError(
                self.error_messages["invalid_choice"],
                code="invalid_choice",
                params={"value": value},
            )

        if value:  # add conditions
            try:
                re.compile(value)
                return value
            except re.error:
                raise exceptions.ValidationError(
                    self.error_messages["invalid_choice"],
                    code="invalid_choice",
                    params={"value": value},
                )

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages['null'],
                                             code='null')

        if not self.blank and value in self.empty_values:
            raise exceptions.ValidationError(self.error_messages['blank'],
                                             code='blank')
