import { FC } from 'react'
import { Box, Flex, Spacer, Text } from '@chakra-ui/react'

import dayjs from 'dayjs'
import 'dayjs/locale/ja'
import relativeTime from 'dayjs/plugin/relativeTime'

import { WaitingTimeHistory } from 'types/WaitingTimeHistories'

dayjs.locale('ja')
dayjs.extend(relativeTime)

const Card: FC<WaitingTimeHistory> = ( post ) => {
    return (
        <Box width="270px" height="165px" borderWidth="1px" borderRadius="lg" overflow="hidden">
            <Box d="flex" alignItems="baseline" bgColor="teal.100" padding={3} paddingBottom="1.5">
                <Spacer />
                <Text fontWeight='bold' fontSize="60">{ post.waiting_time }</Text>
                <Text marginLeft="2">分</Text>
                <Spacer />
            </Box>
            <Flex padding="3" borderTop="1px" borderTopColor="gray.100">
                <Text fontSize="20" marginLeft="1" letterSpacing="wider">{ post.organization.name }</Text>
                <Spacer minWidth="2" />
                <Text margin="auto" color="gray.600" fontSize="12px">{ dayjs( post.created_at ).fromNow() }に更新</Text>
            </Flex>　
        </Box>
    )
}

export default Card