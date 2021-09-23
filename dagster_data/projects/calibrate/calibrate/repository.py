from dagster import repository

from calibrate.pipelines.my_pipeline import my_pipeline
from calibrate.schedules.my_hourly_schedule import my_hourly_schedule
from calibrate.sensors.my_sensor import my_sensor


@repository
def calibrate():
    """
    The repository definition for this calibrate Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    pipelines = [my_pipeline]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return pipelines + schedules + sensors
