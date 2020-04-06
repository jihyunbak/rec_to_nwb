from fl.datamigration.exceptions.invalid_metadata_exception import InvalidMetadataException
from fl.datamigration.exceptions.missing_data_exception import MissingDataException
from fl.datamigration.validation.task_validation_summary import TaskValidationSummary
from fl.datamigration.validation.validator import Validator


class TaskValidator(Validator):

    def __init__(self, tasks):
        self.tasks = tasks

    def createSummary(self):
        if len(self.tasks) == 0:
            raise InvalidMetadataException("There are no tasks defined in metadata.yml file.")
        return TaskValidationSummary(self.tasks)