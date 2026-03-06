import { useEffect, useState } from "react";

export default function DatabasePage() {
  const [pokemon, setPokemon] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/pokemon")
      .then(res => res.json())
      .then(data => {
        setPokemon(data);
      })
      .catch(err => {
        console.error("Failed to fetch Pokémon:", err);
      });
  }, []);

  return (
    <div>
      <h1>Welcome to my Database.</h1>
      <p>Explore the Pokémon and any feedback would be appreciated!</p>

      <ul>
        {pokemon.map(p => (
          <li key={p.id}>{p.name}</li>
        ))}
      </ul>
    </div>
  );
}
