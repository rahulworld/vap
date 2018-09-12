# vap
![python3.x](https://img.shields.io/badge/python-3.x-brightgreen.svg)

> Create 3d visualizations of a city in real-time and analysing data to better living world.

<!-- [Implemented OAT methods](https://github.com/rahulworld/Data-analysis/blob/master/examples/README.md) -->

![3D Visualisation](screenshots/mainpage.png)

Create 3d visualizations of a city in real-time With our 3d visualisation tools you can add 3d models to world wind web and edit their size, angles of heading, pitch, roll and position in real-time. For diaster response, economic planning and controlling through visualisation and mapping. The GDP of the world is growing at a rate of around 3%. And the population of earth is growing at a rate of 1.2%. These rates means that the world needs more cities to house the people who are lifted out of poverty. Moreover in developing world rural population is migrating to urban centres further escalating the need of housing. For these reasons we need to be prepared for the environmental impact these the urban centres will bring to the earth. For this we have developed a 3d visualisation tool where you can visualise the existing cities, neighbourhoods. With World Wind Web we want government and planners to be equipped with a tool where they can easily go through multiple plans.
Our tools can also find empty spaces in cities which are perfectly suitable to plant trees.

### Visualising Existing Areas
Looking cities in 3d can help architectures, planners and government to combat housing shortage by mapping potential areas for buildings and adding 3d models there. Our prediction tools will be able to predict carbon footprint of each building and each neighbourhood. Denser cities means more land left for forests.

### Creating New Areas
With this need of housing existing cities are sprawling to miles and new cities are springing up. With World Wind Web we want government and planners to be equipped with a tool where they can easily go through multiple plans. Our analysis and prediction will be able to predict how much population the 3d plans can hold and how much impact will they have on environment.

### Finding Space For Greenery
Our tools can also find empty spaces in cities which are perfectly suitable to plant trees.

## Getting Started
Leaflet and World Wind Web have been used to build this project.
On leaflet map on the left side you can click and place a footprint indicating the placement of 3d model on the right side World Wind Web.
You have the facility to choose a model from dropdown above. Just select a model and start clicking to place the selected model.
You have the facility to choose a model from dropdown above. Just select a model and start clicking to place the selected model.
You can also edit the scale(which determines the size of the model), heading, roll and pitch(rotation along x, y and z axes).

## How to Navigate
The Left Leaflet Map :- Use the scroll to zoom in or zoom out. Or use the buttons on top left of the map. To move the map around, just drag the map while holding the left click.
The World Wind Map:- Use scroll to zoom in or zoom out. To move the map around, drag the map while holding the left click. To pan around in 3d, drag the map while holding the right click.

### 1. Clone the Repository
```
git clone https://github.com/rahulworld/vap.git
```

### 2. Setup Virtual Environment
```
cd vap
virtualenv venv
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the app
```
python run.py

```
## Future Planning
In future, the facilities to rotate, scale and translate the 3d model will come into place. You will be able to edit the footprint which will immediately scale, rotate or move the 3d model on World Wind Web.
We are also adding the functionality to upload unlimited 3d models to choose from while creating a 3d plan.
And finally you will be able to save these plans, come back, view them and edit them, anytime. We will also provide ways to download entire plans as sketchup or revit files.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/rahulworld/vap. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

To submit a pull request - 

1. Fork/clone the repository.
2. Develop.
3. Create a new branch from the master branch.
4. Open a pull request on Github describing what was fixed or added.
