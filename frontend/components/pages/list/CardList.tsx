import { FC } from 'react'

import { Wrap, WrapItem } from '@chakra-ui/react'
import '@types/WaitingTimeHistories'

import Card from 'components/pages/list/Card'

const CardList: FC = () => {
    return(
        <Wrap padding="10" spacing="30px" justify="center">
        {
            Array(25).fill(0).map(_ => 
                <WrapItem>
                    <Card />
                </WrapItem>
            )
        }
    </Wrap>
    )
}

export default CardList