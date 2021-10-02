import { NextPage } from 'next'
import { useState, useEffect } from 'react'

import { VStack } from '@chakra-ui/layout'

import { WaitingTimeHistoryObject } from 'types/WaitingTimeHistories'

import LoadingMessage from 'components/navigator/LoadingMessage'
import ListControlBar from 'components/pages/list/ListControlBar'
import CardList from 'components/pages/list/CardList'

const List: NextPage = () => {
  const [posts, setPosts] = useState<WaitingTimeHistoryObject>()

    useEffect(() => {
        fetch('http://localhost/api/waiting_time_history/?only-latest=true', {method: 'GET'})
        .then(res => res.json())
        .then(( data: WaitingTimeHistoryObject ) => {
            setPosts(data)
            console.log(data)
        })
    },[])
  if(!posts){
    return <LoadingMessage />
  }
  return(
    <VStack padding="4">
      {/* <ListControlBar /> */}
      <CardList {...posts} />
  </VStack>
  )
}

export default List