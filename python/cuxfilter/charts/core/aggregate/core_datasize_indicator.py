from ..core_chart import BaseChart
from ....layouts import chart_view


class BaseDataSizeIndicator(BaseChart):
    x: str = ""
    use_data_tiles = True

    def __init__(self, width=400, height=400, **library_specific_params):
        """
        Description:

        -------------------------------------------
        Input:
            width
            height
            **library_specific_params
        -------------------------------------------

        Ouput:

        """
        self.height = height
        self.width = width
        self.library_specific_params = library_specific_params

    def initiate_chart(self, dashboard_cls):
        """
        Description:

        -------------------------------------------
        Input:
        data: cudf DataFrame
        -------------------------------------------

        Ouput:

        """
        self.min_value = 0
        self.max_value = len(dashboard_cls._cuxfilter_df.data)

        self.calculate_source(dashboard_cls._cuxfilter_df.data)
        self.generate_chart()

    def view(self):
        return chart_view(self.chart, css_classes=["non-handle-temp"])

    def calculate_source(self, data, patch_update=False):
        """
        Description:

        -------------------------------------------
        Input:

        -------------------------------------------

        Ouput:
        """
        dict_temp = {"X": list([1]), "Y": list([len(data)])}

        self.format_source_data(dict_temp, patch_update)

    def query_chart_by_range(self, active_chart, query_tuple, datatile):
        """
        Description:

        -------------------------------------------
        Input:
            1. active_chart: chart object of active_chart
            2. query_tuple: (min_val, max_val) of the query [type: tuple]
            3. datatile: datatile of active chart for current
                        chart[type:pandas df]
        -------------------------------------------

        Ouput:
        """
        min_val, max_val = query_tuple

        datatile_index_min = int(
            round((min_val - active_chart.min_value) / active_chart.stride)
        )
        datatile_index_max = int(
            round((max_val - active_chart.min_value) / active_chart.stride)
        )

        if datatile_index_min == 0:
            datatile_result = datatile.loc[datatile_index_max].values
        else:
            datatile_index_min -= 1
            datatile_max_values = datatile.loc[datatile_index_max].values
            datatile_min_values = datatile.loc[datatile_index_min].values
            datatile_result = datatile_max_values - datatile_min_values

        self.reset_chart(datatile_result)

    def query_chart_by_indices_for_count(
        self,
        active_chart,
        old_indices,
        new_indices,
        datatile,
        calc_new,
        remove_old,
    ):
        """
        Description:

        -------------------------------------------
        Input:
        -------------------------------------------

        Ouput:
        """
        if len(new_indices) == 0 or new_indices == [""]:
            datatile_result = datatile.cumsum().values[-1]
            return datatile_result

        if len(old_indices) == 0 or old_indices == [""]:
            datatile_result = 0
        else:
            datatile_result = self.get_source_y_axis()

        for index in calc_new:
            index = int(
                round((index - active_chart.min_value) / active_chart.stride)
            )
            datatile_result += datatile.loc[int(index)][0]

        for index in remove_old:
            index = int(
                round((index - active_chart.min_value) / active_chart.stride)
            )
            datatile_result -= datatile.loc[int(index)][0]

        return datatile_result

    def query_chart_by_indices(
        self, active_chart, old_indices, new_indices, datatile
    ):
        """
        Description:

        -------------------------------------------
        Input:
            1. active_chart: chart object of active_chart
            2. query_tuple: (min_val, max_val) of the query [type: tuple]
            3. datatile: datatile of active chart for
                        current chart[type:pandas df]
        -------------------------------------------

        Ouput:
        """
        calc_new = list(set(new_indices) - set(old_indices))
        remove_old = list(set(old_indices) - set(new_indices))

        if "" in calc_new:
            calc_new.remove("")
        if "" in remove_old:
            remove_old.remove("")

        datatile_result = self.query_chart_by_indices_for_count(
            active_chart,
            old_indices,
            new_indices,
            datatile,
            calc_new,
            remove_old,
        )

        self.reset_chart(datatile_result)
