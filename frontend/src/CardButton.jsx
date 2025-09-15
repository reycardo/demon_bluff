import { skull_image } from './config';
import { cardButtonStyle, skullImageStyle, cardImageStyle, cardPositionStyle, cardTemplateStyle } from './styles/styles';

export default function CardButton({ card, x, y, cardSize, selected, onSelect }) {
  return (
    <>
      {/* Template textbox above the button */}
      <textarea
        value={card.template}
        readOnly
        rows={3}
        style={cardTemplateStyle(x, y, cardSize)}
      />
      <button
        key={card.position}
        style={cardButtonStyle(x, y, cardSize, selected, card.position)}
        onClick={() => onSelect(selected === card.position ? null : card.position)}
      >
        <span style={cardPositionStyle}>#{card.position}</span>
        <img
          src={card.is_dead ? card.image : (card.masked_card ? card.masked_card.image : card.image)}
          alt={card.name}
          style={cardImageStyle(cardSize)}
        />
        {card.is_dead && (
          <img
            src={skull_image}
            alt="Killed"
            style={skullImageStyle(cardSize)}
          />
        )}
        <span>{card.masked_card ? card.masked_card.name : card.name}</span>
      </button>
    </>
  );
}
