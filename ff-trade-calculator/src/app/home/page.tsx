"use client";

import React, { useRef, useEffect, useState } from "react";
import { Player, getPlayers, getStaticProps } from "../players/player";

const TradePage: React.FC = async () => {
  //const playerList = await getPlayers('../data/Player_2022_cleaned_copy.csv');
  const serverProps = await getStaticProps();
  const players = serverProps

  useEffect(() => {
    
  });

  return (
    <div>
        {playerList[0].name}
    </div>
  );
};

export default TradePage;