import { FC } from 'react'

import { Wrap, WrapItem } from '@chakra-ui/react'
import { WaitingTimeHistoryObject} from 'types/WaitingTimeHistories'

import Card from 'components/pages/list/Card'

const CardList: FC<WaitingTimeHistoryObject> = (posts) => {
    console.log( Object.keys(posts) )
    return(
        <Wrap padding="10" spacing="30px" justify="center" paddingTop="3">
            {
                Object.keys( posts ).map(
                    key => 
                        <WrapItem key={key}>
                            <Card key={key} {...posts[key] } />
                        </WrapItem>
                    
                )
            }
    </Wrap>
    )
}

export default CardList