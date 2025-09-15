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
  position: 'relative',
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
