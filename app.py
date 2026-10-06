import streamlit as st

from places import places
from bfs import bfs_route
from a_star import a_star_route


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Tourist Route Planner",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ AI Tourist Route Planner")

st.write(
    "Find an efficient route between tourist destinations "
    "using AI search algorithms."
)


# -----------------------------
# User Preferences
# -----------------------------

st.header("👤 Tourist Preferences")

name = st.text_input("Enter your name")

place_list = list(places.keys())

start = st.selectbox(
    "📍 Starting Location",
    place_list
)

destination = st.selectbox(
    "🎯 Destination",
    place_list
)

algorithm = st.selectbox(
    "🤖 Select Route Planning Algorithm",
    ["BFS", "A* Search"]
)


# -----------------------------
# Find Route
# -----------------------------

if st.button("🚀 Find Route"):

    if start == destination:

        st.warning(
            "Starting location and destination "
            "cannot be the same."
        )

    else:

        if algorithm == "BFS":

            route = bfs_route(
                start,
                destination
            )

            if route:

                st.success("BFS Route Found!")

                st.write(
                    " → ".join(route)
                )

                st.write(
                    f"Number of places: {len(route)}"
                )

            else:

                st.error("No route found.")


        elif algorithm == "A* Search":

            route, distance = a_star_route(
                start,
                destination
            )

            if route:

                st.success("A* Route Found!")

                st.write(
                    " → ".join(route)
                )

                st.write(
                    f"Total Distance: {distance} km"
                )

            else:

                st.error("No route found.")