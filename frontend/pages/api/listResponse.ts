import type { NextApiRequest, NextApiResponse } from 'next'

type Data = {
  name: string
  description: string
  wait_time: number
  created_time: Date
}

const threeHundredSecondsAgo = new Date(Date.now() - 300 * 1000)

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  res.status(200).json(
    {
        name: "コンピュータ部",
        description: "部員による展示です",
        wait_time: 25,
        created_time: threeHundredSecondsAgo
    }
  )
}
