export default function CardButton({ card, x, y, cardSize, selected, onSelect }) {
  return (
    <>
      {/* Template textbox above the button */}
      <textarea
        value={card.template}
        readOnly
        rows={3}
        style={{
          position: 'absolute',
          left: x + (cardSize / 2) - (140 / 2),
          top: y - 70,
          width: '140px',
          textAlign: 'center',          
          fontSize: '1rem',
          background: '#000000ff',
          border: '1px solid #ccc',
          borderRadius: '8px',
          marginBottom: '8px',
          padding: '4px 8px',
          zIndex: 2,
          resize: 'none',
          overflow: 'auto',
          whiteSpace: 'pre-wrap',          
        }}
      />
      <button
        key={card.name}
        style={{
          position: 'absolute',
          left: x,
          top: y,
          width: cardSize,
          height: cardSize,
          borderRadius: '50%',
          fontSize: '1.1rem',
          cursor: 'pointer',
          background: selected === card.name ? '#007618ff' : '#000000ff',
          border: '2px solid #888',
          boxShadow: '0 2px 6px rgba(0,0,0,0.1)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          overflow: 'hidden',
          transition: 'background 0.2s'
        }}
  onClick={() => onSelect(selected === card.name ? null : card.name)}
      >
        <img src={card.image} alt={card.name} style={{ width: cardSize * 0.6, height: cardSize * 0.6, objectFit: 'contain', marginBottom: 4 }} />
        <span>{card.name}</span>
      </button>
    </>
  );
}
