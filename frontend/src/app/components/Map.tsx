"use client"; // Ajout pour marquer ce fichier comme un composant client

import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { useEffect } from 'react';
import L from 'leaflet';

const position: [number, number] = [46.603354, 1.888334]; // Coordonnées par défaut (France)

// Correction de l'icône par défaut de Leaflet
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon-2x.png',
  iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
});

const Map = () => {
  useEffect(() => {
    // S'assure que la carte est bien rendue côté client
  }, []);

  return (
    <MapContainer
      center={position}
      zoom={6}
      style={{ height: '100vh', width: '100%' }}
      scrollWheelZoom={false}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <Marker position={position}>
        <Popup>Un lieu spéléo intéressant.</Popup>
      </Marker>
    </MapContainer>
  );
};

export default Map;