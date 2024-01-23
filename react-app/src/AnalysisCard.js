import React from 'react';

const AnalysisCard = ({ name, description, checked, onChange, onClick, selected }) => {
    return (
        <div
            className={`Card ${selected ? 'selected' : ''}`}
            onClick={() => onClick(name)}
        >
            <label>{name}</label>
            <p>{description}</p>
        </div>
    );
};

export default AnalysisCard;
