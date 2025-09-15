export const selectedCardInfoStyle = {
  position: 'absolute',
  left: '50%',
  top: '50%',
  transform: 'translate(-50%, -50%)',
  textAlign: 'center',
  fontSize: '1.2rem',
  minHeight: '2rem',
  maxWidth: '260px',
  margin: '0 auto',
  background: '#000000ff',
  border: '1px solid #ccc',
  borderRadius: '20px',
  padding: '1rem',
  boxShadow: '0 2px 8px rgba(0,0,0,0.08)'
};
export const appContainerStyle = {
  position: 'fixed',
  top: 0,
  left: 0,
  width: '100vw',
  height: '100vh',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  flexDirection: 'column'
};
export const killButtonStyle = {
  marginTop: 24,
  padding: '0.5rem 1.5rem',
  fontSize: '1.1rem',
  borderRadius: 8,
  background: '#c00',
  color: '#fff',
  border: 'none',
  cursor: 'pointer',
};

export const generateGameButtonStyle = {
  position: 'absolute',
  top: 24,
  left: 24,
  zIndex: 100,
  padding: '0.5rem 1.5rem',
  fontSize: '1.1rem',
  borderRadius: 8,
  background: '#007618ff',
  color: '#fff',
  border: 'none',
  cursor: 'pointer'
};

export const cardButtonStyle = (x, y, cardSize, selected, position) => ({
  position: 'absolute',
  left: x,
  top: y,
  width: cardSize,
  height: cardSize,
  borderRadius: '50%',
  fontSize: '1.1rem',
  cursor: 'pointer',
  background: selected === position ? '#007618ff' : '#000000ff',
  border: '2px solid #888',
  boxShadow: '0 2px 6px rgba(0,0,0,0.1)',
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  overflow: 'hidden',
  transition: 'background 0.2s',  
});

export const skullImageStyle = cardSize => ({
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: cardSize * 0.5,
  height: cardSize * 0.5,
  pointerEvents: 'none',
  zIndex: 10,
});

export const cardImageStyle = cardSize => ({
  width: cardSize * 0.6,
  height: cardSize * 0.6,
  objectFit: 'contain',
  marginBottom: 4,
});

export const cardPositionStyle = {
  marginBottom: 8,
  marginTop: 8,
};

export const cardTemplateStyle = (x, y, cardSize) => ({
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
});
