from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
from cache_data import get_data_from_file
from datetime import datetime as dt
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

datafile = "./btc_historical"

"""
Bitcoin DCA calculator
x axis = date, y axis = total amount dca'd
total = sum date start - date end of [amt * frequency]
unit rate = fiat amt / btc rate in fiat
frequency = (daily, weekly, monthly)
Inputs: amount, date range, frequency

Reference: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
"""

LOGO = "https://rates.bitcoin.org.hk/static/images/BAHK_black_square.svg"

# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
#app = Dash(external_stylesheets=[dbc.themes.CYBORG, dbc_css])
app = Dash(external_stylesheets=[dbc.themes.VAPOR, dbc_css])
df = get_data_from_file(datafile)
load_figure_template(["sketchy", "cyborg", "minty", "darkly", "vapor", "slate", "superhero", "quartz"])
template_type = "vapor"


items_bar = dbc.Row(
    [
        dbc.Col(dbc.NavItem(dbc.NavLink("Rates", href="https://rates.bitcoin.org.hk/"))),
        dbc.Col(dbc.NavItem(dbc.NavLink("Sats", href="https://sats.bitcoin.org.hk/"))),
        dbc.Col(dbc.NavItem(dbc.NavLink("Blocks", href="https://blocks.bitcoin.org.hk/"))),
    ],
    className="ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="60px")),
                        dbc.Col(dbc.NavbarBrand("Bitcoin HK", className="ms-2")),
                    ],
                    align="center",
                    # className="g-0",
                ),
                href="https://bitcoin.org.hk",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                items_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ], # className="mt-2 mb-2"
    ),
    color="dark",
    dark=True,
    className=""
)




# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


currency_dropdown = dbc.DropdownMenu(
    label="Currency",
    children=[
        dbc.DropdownMenuItem("HKD"),
        dbc.DropdownMenuItem("USD"),
        dbc.DropdownMenuItem("CNY"),
    ],
)


amount_input = html.Div(
    [
        dbc.Label("Enter Amount: ", className="ms-2"),
        dbc.Input(size="lg", value=100, className="mb-3", type="number", id="amount", min=0, max=1000000, step=1),
        #currency_dropdown
    ]
)


inline_radioitems = html.Div(
    [
        dbc.Label("Select frequency: ", className="ms-2"),
        dbc.RadioItems(
            options=[
                {"label": "Daily", "value": "daily"},
                {"label": "Weekly", "value": "weekly"},
                {"label": "Bi-weekly", "value": "bi-weekly"},
                {"label": "Monthly", "value": "monthly"},
            ],
            value="daily",
            id="freq",
            inline=True,
            className="mb-3"
        ),
    ], className="mt-3 mb-4 mt-md-0"
)

date_range = html.Div(
    [
        dbc.Label("Select Date Range: ",  className="ms-2" ),
        dcc.DatePickerRange(
            id="date-picker",
            min_date_allowed=dt(2022, 1, 1),
            max_date_allowed=dt(2022, 12, 31),
            initial_visible_month=dt(2022, 1, 1),
            start_date=dt(2022, 1, 1),
            end_date=dt(2022, 12, 31),
            className="ms-2",  
        ),
    ], className="mt-3 mb-4 mt-md-0"
)

footer = html.Div([
            html.A(     
                "Source",
                href="https://github.com",
                style={"textDecoration": "none"})
            ], className="mb-4")


app.layout = dbc.Container(
    [
        navbar,
        dbc.Card(
            [
                dbc.Container(
                    [
                        html.Div([
                            html.H1("DCA Calculator", className="display-3"), 
                            #html.H1("DCA Calculator", className="bg-primary text-white p-2 mb-2 text-center"),
                            html.P(
                                "Use utility classes for typography and spacing to suit the "
                                "larger container."
                            ),
                            html.Hr(className="my-2"), 
                        ], className="mt-4 mb-4"),
                        html.Div([
                            amount_input,
                            inline_radioitems,
                            date_range,    
                        ], className=""),
                        html.Div([
                            dcc.Graph(id="graph"),
                        ]), #className="mt-5 mb-4 mt-md-0" ),
                        footer,
                    ]
                )
            ],
        # className="mt-4 mb-4",
        ),
    ],
    fluid=True,
    className="dbc",
)


@app.callback(
    Output("graph", "figure"),
    Input("amount", "value"),
    Input("freq", "value"),
    Input("date-picker", "start_date"),
    Input("date-picker", "end_date"),
)
def display_area(amount, freq, start_date, end_date):
    print(amount, freq, start_date, end_date)

    if amount is not None:
        # calculate dca
        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        fig = px.area(
            filtered_df, x="date", y="usdsat_rate", template=template_type
        )

        return fig


if __name__ == "__main__":
    app.run_server(debug=True)
