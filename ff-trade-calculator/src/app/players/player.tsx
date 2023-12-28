import * as fs from 'fs';
import type { GetServerSideProps } from "next";
import * as csv from 'csv-parser';

enum Position {
  QB = 0,
  RB = 1,
  WR = 2,
  TE = 3,
}

export interface Player {
  name: string;
  team: string;
  picture?: string;
  position: Position;
  points: number;
}

export const getStaticProps: GetServerSideProps = async () => {
  return {
    props: {
      players: getPlayers('../data/Player_2022_cleaned_copy.csv')
    },
  };
};

export function getPlayers(filePath: string): Promise<Player[]> {
  return new Promise((resolve, reject) => {
    const players: Player[] = [];

    fs.createReadStream(filePath)
      .pipe(csv.default())
      .on('data', (row) => {
        const player: Player = {
          name: row.Name,
          team: row.Team,
        //   picture: row.picture,
          position: row.Pos as Position,
          points: row.Total_Pts, 
        };

        players.push(player);
      })
      .on('end', () => {
        resolve(players);
      })
      .on('error', (error) => {
        reject(error);
      });
  });
}

// Example usage
const csvFilePath = '../data/Player_2022_cleaned_copy.csv';

// readCsv(csvFilePath)
//   .then((players) => {
//     console.log(players);
//     // Now you have an array of player objects
//   })
//   .catch((error) => {
//     console.error('Error reading CSV file:', error);
//   });
