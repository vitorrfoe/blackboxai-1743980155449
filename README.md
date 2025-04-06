
Built by https://www.blackbox.ai

---

```markdown
# Localizador Compartilhado

## Project Overview
Localizador Compartilhado is a web application that enables users to share their real-time location through generated links. With a focus on simplicity, the app allows users to create unique links that can be shared with friends or family. The app utilizes geolocation to display the user's current position on a map, providing additional context and information about the location.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/localizador-compartilhado.git
   cd localizador-compartilhado
   ```
   
2. **Open the `index.html` file** in your web browser:
   Simply double-click on `index.html` or right-click and choose to open it with your preferred browser.

## Usage
1. Open the application in your web browser.
2. Enter a name for your link in the "Nome do Link" input field.
3. Click on "Gerar Link" to create a shareable link.
4. The generated link will appear; you can copy it by clicking the copy button next to it.
5. Share the link with others. When they access it, they'll be able to see your real-time location on the map.

## Features
- Generate a unique link for real-time location sharing.
- Display current location on an interactive map using Leaflet.
- Display geographical coordinates (latitude and longitude).
- Reverse geocoding to obtain and display the address.
- Beautiful UI with responsive design and Tailwind CSS integration.

## Dependencies
The project has the following dependencies loaded through CDNs:
- **Tailwind CSS**: A utility-first CSS framework for styling.
- **Font Awesome**: A font and icon toolkit for scalable vector icons.
- **Leaflet**: A JavaScript library for interactive maps.
- **Nominatim**: An OpenStreetMap tool for reverse geocoding (used in the script for obtaining addresses).

## Project Structure
```
localizador-compartilhado/
├── index.html              # Main HTML file for link generation
├── track.html              # HTML file for tracking location
├── styles.css              # Custom CSS styles for the application
```

### File Descriptions
- `index.html`: Contains the user interface for link generation, including input fields and buttons. The generated link is used to share the user's location.
- `track.html`: Responsible for displaying the user's location on a Leaflet map and retrieving geographical information using the generated link's tracking code.
- `styles.css`: Contains custom styles and animations for the application.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
```